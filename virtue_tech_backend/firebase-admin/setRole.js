// Run this file manually to assign roles

const admin = require("firebase-admin");
const serviceAccount = require("./serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
});

// --- CHANGE THESE --- //
const uid = "PUT_USER_UID_HERE";
const role = "student"; // student, teacher, parent, admin
// --------------------- //

admin
  .auth()
  .setCustomUserClaims(uid, { role })
  .then(() => {
    console.log("Role updated successfully!");
    process.exit(0);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
