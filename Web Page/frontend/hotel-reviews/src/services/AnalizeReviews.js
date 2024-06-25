const API_URL = "http://127.0.0.1:8000";

const analyzeReview = async (text, hotel_id) => {
  try {
    const response = await fetch(`${API_URL}/api/keras-predict/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text, hotel_id }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
};

export default analyzeReview;
