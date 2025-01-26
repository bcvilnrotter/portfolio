---
layout: default
title: "About Me"
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --accent-color: #e74c3c;
            --text-color: #2c3e50;
            --background-color: #f8f9fa;
            --card-background: #ffffff;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--background-color);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        .title {
            font-size: 3rem;
            margin-bottom: 2rem;
            color: var(--primary-color);
            animation: fadeInDown 1s ease-out;
            text-align: center;
        }

        .subtitle {
            font-size: 1.5rem;
            color: var(--secondary-color);
            margin-bottom: 2rem;
            animation: fadeInUp 1s ease-out 0.3s backwards;
            text-align: center;
        }

        .card {
            background: var(--card-background);
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
            transform: translateY(0);
            transition: transform 0.3s ease;
            animation: fadeIn 1s ease-out 0.6s backwards;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .cta-button {
            display: inline-block;
            padding: 1rem 2rem;
            background-color: var(--secondary-color);
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 2rem;
            transition: background-color 0.3s ease;
            animation: fadeIn 1s ease-out 0.9s backwards;
        }

        .cta-button:hover {
            background-color: var(--primary-color);
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        @media (max-width: 768px) {
            .container {
                padding: 1rem;
            }
            
            .title {
                font-size: 2rem;
            }
            
            .subtitle {
                font-size: 1.2rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">About Me</h1>
        <p class="subtitle">Digital Forensics & Data Science Journey</p>
        
        <div class="card">
            <p>Thank you for visiting my portfolio. I am an incident response analyst with a decade of experience in Digital Forensics and Incident Response (DFIR), currently embarking on an exciting transition into Data Science and Machine Learning.</p>
            <p>With over a decade of Python programming experience, I specialize in developing automations and forensic tools that enhance investigative efficiency. My background in DFIR provides a unique perspective on data analysis and problem-solving.</p>
            <p>This site is actively being developed to showcase my journey and projects. You can follow my progress and see real-time updates on my transition into the data science field.</p>
            <a href="journey" class="cta-button">Follow My Journey</a>
        </div>
    </div>
</body>
</html>
