/**
 * =========================================================================
 * GOOGLE APPS SCRIPT: AUTO-SAVE WEBSITE MESSAGES TO GOOGLE SHEETS
 * Owner Email: mdmirazahmed3690@gmail.com
 * Features:
 *  1. Auto-records: ID, Date & Time, Client Name, Client Email, Project Message
 *  2. Auto-Pagination: When a sheet reaches 50 rows, it automatically 
 *     creates a new page/tab (e.g. "Page 1", "Page 2", "Page 3")
 *  3. Email Alert: Automatically sends an alert to mdmirazahmed3690@gmail.com
 * =========================================================================
 */

var MAX_ROWS_PER_PAGE = 50; // প্রতি পেজে ৫০টি মেসেজ জমা হলে নতুন পেজ/ট্যাব খুলবে

function doPost(e) {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var data = {};
    
    if (e.postData && e.postData.contents) {
      data = JSON.parse(e.postData.contents);
    } else if (e.parameter) {
      data = e.parameter;
    }

    var name = data.name || "Unknown Client";
    var email = data.email || "No Email Provided";
    var message = data.message || "No Message Text";
    var dateFormatted = data.dateFormatted || new Date().toLocaleString("en-US", { timeZone: "Asia/Dhaka" });
    var msgId = data.id || ("msg-" + new Date().getTime());

    // 1. Get or Create the right page/tab
    var sheet = getTargetSheet(ss);

    // 2. Append the new message row
    sheet.appendRow([msgId, dateFormatted, name, email, message]);

    // 3. Optional: Send Instant Email Notification to mdmirazahmed3690@gmail.com
    try {
      MailApp.sendEmail({
        to: "mdmirazahmed3690@gmail.com",
        subject: "New Portfolio Inquiry from: " + name,
        htmlBody: "<h2>New Client Message Received!</h2>" +
                  "<p><strong>Name:</strong> " + name + "</p>" +
                  "<p><strong>Email:</strong> " + email + "</p>" +
                  "<p><strong>Date & Time:</strong> " + dateFormatted + "</p>" +
                  "<p><strong>Project Details:</strong></p>" +
                  "<blockquote style='background:#f3f4f6;padding:12px;border-left:4px solid #FF2A3B;'>" + message + "</blockquote>" +
                  "<p><em>Saved automatically to your Google Sheet (" + sheet.getName() + ").</em></p>"
      });
    } catch (mailErr) {
      Logger.log("Email notify skipped: " + mailErr);
    }

    return ContentService.createTextOutput(JSON.stringify({
      status: "success",
      sheet: sheet.getName(),
      rows: sheet.getLastRow()
    })).setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({
      status: "error",
      message: error.toString()
    })).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet(e) {
  return ContentService.createTextOutput(JSON.stringify({
    status: "online",
    message: "Google Sheets Webhook for mdmirazahmed3690@gmail.com is active!"
  })).setMimeType(ContentService.MimeType.JSON);
}

// Helper: Finds current active page or creates "Page X" when full
function getTargetSheet(ss) {
  var sheets = ss.getSheets();
  var targetSheet = null;

  // Find the latest "Page X" or "Messages" tab
  for (var i = sheets.length - 1; i >= 0; i--) {
    var s = sheets[i];
    var sName = s.getName();
    if (sName.indexOf("Page ") === 0 || sName === "Messages" || sName === "Sheet1") {
      targetSheet = s;
      break;
    }
  }

  // If no sheet found, create Page 1
  if (!targetSheet) {
    targetSheet = ss.insertSheet("Page 1");
    setupHeader(targetSheet);
    return targetSheet;
  }

  // If first sheet was default Sheet1, rename it to Page 1 and setup header
  if (targetSheet.getName() === "Sheet1" && targetSheet.getLastRow() <= 1) {
    targetSheet.setName("Page 1");
    setupHeader(targetSheet);
    return targetSheet;
  }

  // Check if current sheet has reached the maximum rows limit
  if (targetSheet.getLastRow() >= (MAX_ROWS_PER_PAGE + 1)) {
    // Current page is FULL! Create a new page tab!
    var pageNum = 2;
    var match = targetSheet.getName().match(/Page\s+(\d+)/);
    if (match) {
      pageNum = parseInt(match[1], 10) + 1;
    }
    
    var newSheetName = "Page " + pageNum;
    targetSheet = ss.insertSheet(newSheetName);
    setupHeader(targetSheet);
  }

  return targetSheet;
}

// Formats and adds header row with styling
function setupHeader(sheet) {
  if (sheet.getLastRow() === 0) {
    var headers = ["ID", "তারিখ ও সময় (Date & Time)", "ক্লায়েন্টের নাম (Client Name)", "ইমেইল (Client Email)", "মেসেজ / প্রজেক্ট বিবরণ (Project Message)"];
    sheet.appendRow(headers);
    
    var headerRange = sheet.getRange(1, 1, 1, headers.length);
    headerRange.setBackground("#111827");
    headerRange.setFontColor("#FFFFFF");
    headerRange.setFontWeight("bold");
    headerRange.setHorizontalAlignment("center");
    
    sheet.setColumnWidth(1, 140);
    sheet.setColumnWidth(2, 180);
    sheet.setColumnWidth(3, 180);
    sheet.setColumnWidth(4, 200);
    sheet.setColumnWidth(5, 450);
    sheet.setFrozenRows(1);
  }
}
