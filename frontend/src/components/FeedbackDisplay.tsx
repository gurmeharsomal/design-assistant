import React from "react";

interface FeedbackDisplayProps {
  feedback: string;
}

const FeedbackDisplay: React.FC<FeedbackDisplayProps> = ({ feedback }) => {
  return (
    <div>
      <h3>Feedback:</h3>
      {feedback ? <p>{feedback}</p> : <p>No feedback available</p>}
    </div>
  );
};

export default FeedbackDisplay;