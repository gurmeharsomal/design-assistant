import React from "react";
import "./App.css";
import ImageUpload from "./components/ImageUpload";  

const App: React.FC = () => {
  return (
    <div className="App">
      <h1>Design Feedback Assistant</h1>
      <ImageUpload />
    </div>
  );
};

export default App;
