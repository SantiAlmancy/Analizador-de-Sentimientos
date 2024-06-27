import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import Header from '../components/Header';
import './AddReview.css';
import {analyzeReview, analyzeReviewTransformer} from '../services/AnalizeReviews';

const AddReview = () => {
    const { id } = useParams();
    const [review, setReview] = useState({
        value: '',  // Initially empty
        text: ''
    });
    const [showValue, setShowValue] = useState(false);  // State to control visibility

    const handleChange = (e) => {
        const { name, value } = e.target;
        setReview(prevReview => ({
            ...prevReview,
            [name]: value
        }));
    };

    const handleButtonClick = async () => {
        try {
            const data = await analyzeReview(review.text, id);
            setReview(prevReview => ({
                ...prevReview,
                value: data.value  // Update the value with the prediction result
            }));
            setShowValue(true);  // Show the value when button is clicked
        } catch (error) {
            console.error('Error fetching review category:', error);
        }
    };

    const handleButtonClickTransformer = async () => {
        try {
            const data = await analyzeReviewTransformer(review.text, id);
            setReview(prevReview => ({
                ...prevReview,
                value: data.value  // Update the value with the prediction result
            }));
            setShowValue(true);  // Show the value when button is clicked
        } catch (error) {
            console.error('Error fetching review category:', error);
        }
    };

    return (
        <div className='addReview'>
            <Header text={"Hotel Reviews"} showButton={true} />
            <div className="addReviewContainer">
                <h1>Add Review for Hotel: {id}</h1>
                <form>
                    <label>
                        Review Text:
                        <textarea name="text" value={review.text} onChange={handleChange} />
                    </label>
                    <div className="buttonContainer">
                        <button type="button" className='button' onClick={handleButtonClick}>Check Review (Keras)</button>
                        <button type="button" className='button' onClick={handleButtonClickTransformer}>Check Review (Transformer)</button>
                    </div>
                    {showValue && <p>Value: {review.value}</p>}
                </form>
            </div>
        </div>
    );
};

export default AddReview;