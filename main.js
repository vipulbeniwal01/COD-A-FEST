import { GoogleGenerativeAI } from "@google/generative-ai";

const  genai = new GoogleGenerativeAI("AIzaSyBnut3BNZYCY6cfIKyf33jJYyi7yySztwE");

const model = genai.getGenerativeModel({
  model : "gemini-1.5-pro"
});

const r = await model.generateContent("What is node js?");

console.log(r.response.text());

// <<<<<<< main

// // hello new comment
// =======
// commmit
// >>>>>>> main
