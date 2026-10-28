const http = require('http');
const https = require('https');
const fs = require('fs');
const path = require('path');

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.json': 'application/json',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm',
  '.ico': 'image/x-icon',
  '.pdf': 'application/pdf'
};

const REVIEWS_FILE = path.join(__dirname, 'data', 'reviews.json');
const MESSAGES_FILE = path.join(__dirname, 'data', 'messages.json');
const CONFIG_FILE = path.join(__dirname, 'data', 'config.json');

function forwardToGoogleSheet(payload) {
  try {
    if (!fs.existsSync(CONFIG_FILE)) return;
    const cfg = JSON.parse(fs.readFileSync(CONFIG_FILE, 'utf-8'));
    const webhookUrl = (cfg.google_sheet_webhook_url || '').trim();
    if (!webhookUrl || !webhookUrl.startsWith('http')) return;

    const data = JSON.stringify(payload);
    const parsedUrl = new URL(webhookUrl);
    
    const client = parsedUrl.protocol === 'https:' ? https : http;
    const options = {
      hostname: parsedUrl.hostname,
      path: parsedUrl.pathname + parsedUrl.search,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data)
      }
    };

    const forwardReq = client.request(options, (forwardRes) => {
      console.log(`[Google Sheet Sync] Forwarded to Google Sheet! Status: ${forwardRes.statusCode}`);
    });

    forwardReq.on('error', (e) => {
      console.warn('[Google Sheet Sync Error]', e.message);
    });

    forwardReq.write(data);
    forwardReq.end();
  } catch (err) {
    console.warn('[Google Sheet Forward Exception]', err.message);
  }
}

function setCorsHeaders(res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
}

const server = http.createServer((req, res) => {
  setCorsHeaders(res);

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  const urlObj = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  const pathname = urlObj.pathname;

  // ==========================================
  // API: GET /api/messages (Admin view)
  // ==========================================
  if (pathname === '/api/messages' && req.method === 'GET') {
    fs.readFile(MESSAGES_FILE, 'utf-8', (err, data) => {
      if (err) {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify([]));
        return;
      }
      res.writeHead(200, {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
      });
      res.end(data);
    });
    return;
  }

  // ==========================================
  // API: POST /api/contact
  // ==========================================
  if (pathname === '/api/contact' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk;
      if (body.length > 50000) {
        req.destroy();
      }
    });

    req.on('end', () => {
      try {
        const payload = JSON.parse(body);
        const name = (payload.name || '').trim();
        const email = (payload.email || '').trim();
        const message = (payload.message || '').trim();

        if (!name || !message) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Name and message are required.' }));
          return;
        }

        const newMessage = {
          id: 'msg-' + Date.now(),
          name: name.slice(0, 100),
          email: email.slice(0, 100),
          message: message.slice(0, 1500),
          timestamp: new Date().toISOString(),
          dateFormatted: new Date().toLocaleString('en-US', { timeZone: 'Asia/Dhaka' })
        };

        let messages = [];
        if (fs.existsSync(MESSAGES_FILE)) {
          try {
            messages = JSON.parse(fs.readFileSync(MESSAGES_FILE, 'utf-8'));
          } catch (e) {
            messages = [];
          }
        }

        messages.unshift(newMessage);
        fs.writeFileSync(MESSAGES_FILE, JSON.stringify(messages, null, 2), 'utf-8');

        console.log(`[Contact Message Saved] From "${name}" (${email}): "${message.slice(0, 60)}..."`);
        
        // Auto-forward to Google Sheets under mdmirazahmed3690@gmail.com
        forwardToGoogleSheet(newMessage);

        res.writeHead(201, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, message: newMessage }));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON payload.' }));
      }
    });
    return;
  }

  // ==========================================
  // API: GET /api/reviews
  // ==========================================
  if (pathname === '/api/reviews' && req.method === 'GET') {
    fs.readFile(REVIEWS_FILE, 'utf-8', (err, data) => {
      if (err) {
        res.writeHead(200, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify([]));
        return;
      }
      res.writeHead(200, {
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
      });
      res.end(data);
    });
    return;
  }

  // ==========================================
  // API: POST /api/reviews
  // ==========================================
  if (pathname === '/api/reviews' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => {
      body += chunk;
      if (body.length > 50000) {
        req.destroy();
      }
    });

    req.on('end', () => {
      try {
        const payload = JSON.parse(body);
        const name = (payload.name || '').trim();
        const role = (payload.role || '').trim() || 'Verified Client';
        const reviewText = (payload.review || '').trim();
        const rating = Math.min(5, Math.max(1, parseInt(payload.rating, 10) || 5));

        if (!name || !reviewText) {
          res.writeHead(400, { 'Content-Type': 'application/json' });
          res.end(JSON.stringify({ error: 'Name and review text are required.' }));
          return;
        }

        const newReview = {
          id: 'rev-' + Date.now(),
          name: name.slice(0, 60),
          role: role.slice(0, 60),
          review: reviewText.slice(0, 500),
          rating: rating,
          avatar: `https://api.dicebear.com/7.x/initials/svg?seed=${encodeURIComponent(name)}&backgroundColor=FF2A3B&textColor=ffffff`,
          date: new Date().toISOString().split('T')[0]
        };

        let reviews = [];
        if (fs.existsSync(REVIEWS_FILE)) {
          try {
            reviews = JSON.parse(fs.readFileSync(REVIEWS_FILE, 'utf-8'));
          } catch (e) {
            reviews = [];
          }
        }

        // Add to beginning of array so newest review displays first
        reviews.unshift(newReview);
        fs.writeFileSync(REVIEWS_FILE, JSON.stringify(reviews, null, 2), 'utf-8');

        console.log(`[Review Received] New review from "${name}" (${rating} stars): "${reviewText}"`);

        res.writeHead(201, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ success: true, review: newReview }));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'application/json' });
        res.end(JSON.stringify({ error: 'Invalid JSON payload.' }));
      }
    });
    return;
  }

  // ==========================================
  // Static Files Server
  // ==========================================
  let reqPath = decodeURIComponent(pathname);
  if (reqPath === '/' || reqPath === '') reqPath = '/index.html';
  
  const filePath = path.join(__dirname, reqPath);

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain' });
      res.end('404 Not Found');
      return;
    }

    const ext = path.extname(filePath).toLowerCase();
    res.writeHead(200, {
      'Content-Type': MIME[ext] || 'application/octet-stream',
      'Cache-Control': 'no-cache'
    });
    fs.createReadStream(filePath).pipe(res);
  });
});

const PORT = 8080;
server.listen(PORT, '0.0.0.0', () => {
  console.log(`Port ${PORT} server started: http://localhost:${PORT}`);
});
