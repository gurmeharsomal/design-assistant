import axios from "axios";

const API_URL = "http://localhost:8000/api/feedback";

interface FeedbackResponse {
  feedback: string;
}

export const fetchFeedback = async (
  imageData: File | string,
  prompt: string
): Promise<FeedbackResponse> => {
  const formData = new FormData();

  if (imageData instanceof File) {
    // Handle file upload
    formData.append("file", imageData);
  } else if (imageData.startsWith("http")) {
    // Handle image URL
    formData.append("image_url", imageData);
  } else {
    // Handle base64 image data
    formData.append("image_base64", imageData);
  }

  formData.append("prompt", prompt);

  // Use axios with a typed response
  const response = await axios.post<FeedbackResponse>(API_URL, formData, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });

  return response.data;
};