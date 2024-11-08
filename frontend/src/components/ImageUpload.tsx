import React, { useState } from "react";
import { fetchFeedback } from "../api";
import FeedbackDisplay from "./FeedbackDisplay";
import "./ImageUpload.css";

const ImageUpload: React.FC = () => {
  const [image, setImage] = useState<File | null>(null);
  const [prompt, setPrompt] = useState<string>("");
  const [feedback, setFeedback] = useState<string>("");
  const [loading, setLoading] = useState<boolean>(false);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      setImage(e.target.files[0]);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setFeedback(""); 

    if (!image) {
      console.error("No image uploaded.");
      setLoading(false);
      return;
    }

    try {
      const feedbackData = await fetchFeedback(image, prompt);
      setFeedback(feedbackData.feedback);
    } catch (error) {
      console.error("Error fetching feedback:", error);
    }
    setLoading(false); 
  };

  return (
    <div className="image-upload-container">
      <h2>Upload an Image for Feedback</h2>
      <h3>Please note: Uploading smaller image will provide faster feedback.</h3>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Upload Image Here:</label>
          <input type="file" accept="image/*" onChange={handleFileChange} />
        </div>
        <div className="form-group">
          <label>Optional Prompt:</label>
          <textarea
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter a prompt (optional)"
          />
        </div>
        <button type="submit">Get Feedback</button>
      </form>

      {loading ? (
        <div className="loading-spinner">Loading...</div>
      ) : (
        <FeedbackDisplay feedback={feedback} />
      )}
    </div>
  );
};

export default ImageUpload;