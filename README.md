 **"Authorized Keywords Search on Encrypted Data"** with **Python, AES, and Time-Controlled Keyword Privacy** 🚀  

---

## **📌 Project Overview**  
This project focuses on **securely searching encrypted data** while ensuring that only **authorized users** can search using specific keywords for a **limited time**.  

### **🔐 Why is this needed?**  
- When sensitive data (e.g., medical records, financial transactions) is stored in encrypted form, **searching within encrypted data** becomes a challenge.  
- Traditional search methods **expose keywords** to the database or third parties, leading to potential security risks.  
- This project **solves the problem** by:  
  ✅ Allowing **secure keyword searches on encrypted data**  
  ✅ Ensuring **only authorized users** can search specific keywords  
  ✅ Limiting **keyword exposure to a predefined duration**  

---

## **⚙️ How Does It Work?**  

### **Step 1: Data Encryption (AES)**
- Before storing data, **AES encryption** is applied to protect it from unauthorized access.  
- Example:  
  - **Original Data:** `"John's salary is $5000"`  
  - **Encrypted Data:** `"89f3b7e3a5c1d4..."` (AES ciphertext)  
- Encrypted data is stored in a database, ensuring that no one can access it without the decryption key.  

### **Step 2: Secure Keyword Indexing**
- Instead of storing plaintext keywords, a **secure keyword index** is created.  
- Example:  
  - **Keyword:** `"salary"`  
  - **Encrypted Keyword Index:** `"3a7f9c..."`  
- The system ensures that only **authorized users** have access to these keywords.  

### **Step 3: Authorized Keyword Search**
- A user requests to search for a keyword.  
- The system **verifies user authorization** before decrypting the keyword.  
- If the user is **authorized and within the allowed time**, the system **searches for matches in encrypted data**.  
- Results are **decrypted and returned** to the user.  

### **Step 4: Time-Controlled Privacy**
- The **keyword authorization expires** after a set duration (e.g., 24 hours).  
- After expiration, the user **must request access again** to search the keyword.  

---

## **🛠️ Technologies Used**
🔹 **Python** – Core implementation  
🔹 **AES (PyCryptodome)** – Encrypts data & keywords  
🔹 **Flask** (Optional) – API for keyword search requests  
🔹 **SQLite/MongoDB** – Stores encrypted data & keyword indexes  
🔹 **Timer Mechanism** – Controls keyword expiration  

## **🔑 Security Benefits**  
✅ **Prevents unauthorized access** to sensitive data  
✅ **Protects keyword privacy** by avoiding plaintext keyword storage  
✅ **Minimizes risk of data leaks** with **time-controlled search access**  
✅ **Ensures confidentiality** while allowing secure search operations  

---

## **💡 Real-World Applications**
- **Cloud Storage Security** – Secure searching within encrypted cloud data  
- **Healthcare Data Protection** – Encrypted medical records with controlled access  
- **Financial Data Security** – Prevents exposure of sensitive financial transactions  

---
