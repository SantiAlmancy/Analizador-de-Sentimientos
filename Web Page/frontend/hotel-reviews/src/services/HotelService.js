const API_URL = "http://127.0.0.1:3001";

const getHotels = async () => {
    try {
      console.log(`${API_URL}/api/hotels`);
      const response = await fetch(`${API_URL}/api/hotels`);
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
  
  export default getHotels;
