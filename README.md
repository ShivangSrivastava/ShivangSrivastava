<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Profile</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #1e1e1e;
            color: #ddd;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .profile-card {
            background: #2b2b2b;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            max-width: 400px;
            width: 100%;
            text-align: center;
            padding: 20px;
            transition: transform 0.3s, box-shadow 0.3s;
            animation: fadeIn 1s ease-in-out;
        }
        .profile-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5);
        }
        .profile-img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin: 0 auto 20px;
            border: 5px solid #444;
            transition: border-color 0.3s, transform 0.3s, box-shadow 0.3s;
            animation: pulse 2s infinite;
        }
        .profile-img:hover {
            border-color: #666;
            transform: rotate(-5deg) scale(1.05);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.5);
        }
        .profile-name {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
            transition: color 0.3s, text-shadow 0.3s;
        }
        .profile-name:hover {
            color: #ff6b6b; /* Modern Red */
            text-shadow: 0 0 10px rgba(255, 107, 107, 0.7);
        }
        .profile-title {
            font-size: 18px;
            color: #bbb;
            margin-bottom: 20px;
            transition: color 0.3s, text-shadow 0.3s;
        }
        .profile-title:hover {
            color: #61dafb; /* Modern Blue */
            text-shadow: 0 0 10px rgba(97, 218, 251, 0.7);
        }
        .profile-details {
            font-size: 16px;
            color: #999;
            margin-bottom: 20px;
        }
        .profile-details p:nth-child(1) {
            color: #51cc57; /* Modern Green */
        }
        .tech-stack {
            margin-bottom: 20px;
        }
        .tech-stack span {
            display: inline-block;
            background: #444;
            color: #ddd;
            padding: 5px 10px;
            border-radius: 5px;
            margin: 5px;
            transition: background 0.3s, transform 0.3s;
            animation: fadeIn 1s ease-in-out;
        }
        .tech-stack span:hover {
            background: #555;
            transform: scale(1.1);
        }
        .social-links a {
            text-decoration: none;
            margin: 0 10px;
            color: #61dafb; /* Modern Blue */
            transition: color 0.3s;
            animation: fadeIn 1s ease-in-out;
        }
        .social-links a:hover {
            color: #21a1f1;
        }
        .contact-button {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #ff6b6b; /* Modern Red */
            color: white;
            border-radius: 5px;
            text-decoration: none;
            transition: background 0.3s;
            animation: fadeIn 1s ease-in-out;
        }
        .contact-button:hover {
            background: #e63946;
        }
    </style>
</head>
<body>
  <div class="profile-card">
    <img src="https://avatars.githubusercontent.com/u/114788987?v=4" alt="Profile Image" class="profile-img">
    <div class="profile-name">Shivang Srivastava</div>
    <div class="profile-title">Aspiring Full-stack Developer | Node.js, Flutter, & TypeScript</div>
    <div class="profile-details">
        <p>🌟 Passionate about building web and mobile applications.</p>
        <p>💼 Open to new opportunities and collaborations.</p>
    </div>
    <div class="tech-stack">
        <span>Node.js</span>
        <span>Flutter</span>
        <span>TypeScript</span>
        <span>JavaScript</span>
    </div>
    <div class="social-links">
        <a href="https://github.com/ShivangSrivastava" target="_blank">GitHub</a>
        <a href="https://www.linkedin.com/in/shivang-srivastava-developer/" target="_blank">LinkedIn</a>
        <a href="https://www.leetcode.com/shivangsrivastava">LeetCode</a>
        <a href="mailto:shivangsrivastava157@gmail.com">Email</a>
    </div>
    <a href="mailto:shivangsrivastava157@gmail.com" class="contact-button">Contact Me</a>
</div>
</body>
</html>
