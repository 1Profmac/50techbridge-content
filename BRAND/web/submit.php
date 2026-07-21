<?php
/**
 * Digital Pioneer Gallery — Application Form Handler
 * Receives POST from index.html apply form
 * Emails structured application to hello@learnmoretechnologies.com
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://digitalpioneer.ai');
header('Access-Control-Allow-Methods: POST');

// Only accept POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok' => false, 'error' => 'Method not allowed']);
    exit;
}

// Basic honeypot / spam check
if (!empty($_POST['_gotcha'])) {
    http_response_code(200);
    echo json_encode(['ok' => true]); // Silent discard
    exit;
}

// Sanitize helper
function clean($val) {
    return htmlspecialchars(strip_tags(trim($val ?? '')), ENT_QUOTES, 'UTF-8');
}

// Collect fields
$name        = clean($_POST['full_name'] ?? '');
$email       = filter_var($_POST['email'] ?? '', FILTER_SANITIZE_EMAIL);
$age_range   = clean($_POST['age_range'] ?? '');
$years_exp   = clean($_POST['years_experience'] ?? '');
$ethnicity   = clean($_POST['ethnicity'] ?? '');
$discipline  = clean($_POST['creative_discipline'] ?? '');
$tech_level  = clean($_POST['tech_level'] ?? '');
$challenge   = clean($_POST['biggest_challenge'] ?? '');
$barriers    = isset($_POST['barrier']) ? (array)$_POST['barrier'] : [];
$barriers    = implode(', ', array_map('clean', $barriers)) ?: 'None listed';
$referral    = clean($_POST['referral_source'] ?? '');
$eligibility = clean($_POST['eligibility_confirmed'] ?? '');

// Validate required fields
if (!$name || !filter_var($email, FILTER_VALIDATE_EMAIL) || !$age_range || !$ethnicity || !$tech_level || !$challenge) {
    http_response_code(422);
    echo json_encode(['ok' => false, 'error' => 'Missing required fields']);
    exit;
}

// Build email
$to      = 'hello@learnmoretechnologies.com';
$subject = "Digital Pioneer Gallery Application — {$name}";

$body = "
NEW APPLICATION — DIGITAL PIONEER GALLERY
==========================================
Submitted: " . date('F j, Y g:i A T') . "

APPLICANT
---------
Name:         {$name}
Email:        {$email}
Age Range:    {$age_range}
Identity:     {$ethnicity}

CREATIVE PROFILE
----------------
Discipline:   {$discipline}
Experience:   {$years_exp}
Tech Level:   {$tech_level}

CHALLENGE (most important)
--------------------------
{$challenge}

PARTICIPATION BARRIERS
----------------------
{$barriers}

HOW THEY HEARD
--------------
{$referral}

ELIGIBILITY
-----------
Confirmed:    {$eligibility}

==========================================
Reply directly to this email to contact the applicant.
";

$headers  = "From: Digital Pioneer Gallery <noreply@digitalpioneer.ai>\r\n";
$headers .= "Reply-To: {$name} <{$email}>\r\n";
$headers .= "X-Mailer: PHP/" . phpversion();

// Send
$sent = mail($to, $subject, $body, $headers);

if ($sent) {
    // Auto-confirm to applicant
    $confirm_subject = "You applied to the Digital Pioneer Gallery — we'll be in touch";
    $confirm_body = "Hi {$name},

Thank you for applying to the Digital Pioneer Gallery.

We review every application personally and will respond within 5 business days.

In the meantime, follow us for program updates:
→ Instagram / Facebook: @digitalpioneer.ai
→ Questions? Email us at hello@learnmoretechnologies.com

— Brian McKinney
Founder, Digital Pioneer Gallery & Learn More Technologies
MBE Certified · City of Austin ACME Elevate Partner
";
    $confirm_headers  = "From: Digital Pioneer Gallery <hello@learnmoretechnologies.com>\r\n";
    $confirm_headers .= "X-Mailer: PHP/" . phpversion();
    mail($email, $confirm_subject, $confirm_body, $confirm_headers);

    http_response_code(200);
    echo json_encode(['ok' => true]);
} else {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'Mail delivery failed']);
}
?>
