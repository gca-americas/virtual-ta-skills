**Before You Start**
Use a personal Gmail account. Corporate or school-managed accounts will NOT work.
Use Google Chrome in Incognito mode to prevent account conflicts.
**Step 1: Claim Credits**
Open a new Incognito window, paste your event link, and sign in with your personal Gmail.
Click below to copy your special event link:
https://goo.gle/handsonai-waybackhome

Accept the Google Cloud Platform Terms of Service. Once applied, you'll see the message showing the credit has applied.
Credit Applied Screenshot
If prompted to enter credit card information, you can safely ignore it and proceed.

**Step 2: Environment Setup**
In the same Incognito window, go to:
console.cloud.google.com
Click Activate Cloud Shell at the top of the Google Cloud Console (it's the terminal icon in the top-right navigation bar).
In the terminal, run the following commands to clone the setup repository and navigate to the project:

```bash
cd ~
rm -rf handsonai-credit
git clone https://github.com/google-americas/handsonai-credit.git
cd handsonai-credit
chmod +x init.sh
./init.sh
```