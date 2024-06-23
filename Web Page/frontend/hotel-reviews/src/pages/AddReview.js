import React, { useState } from 'react';
import { useParams } from 'react-router-dom';
import './AddReview.css';

const AddReview = ({ props }) => {
    const { id } = useParams();
    const [review, setReview] = useState({
        value: 'Positive',  // Static value
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

    const handleSubmit = (e) => {
        e.preventDefault();
        // Handle the form submission logic here
        props.onSubmit(id, review);  // Pass the review data to the parent component
    };

    const handleButtonClick = () => {
        setShowValue(true);  // Show the value when button is clicked
    };

    return (
        <div className="addReview">
            <h1>Add Review for Hotel: {id}</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Review Text:
                    <textarea name="text" value={review.text} onChange={handleChange} />
                </label>
                <button type="button" onClick={handleButtonClick}>Check Review's Category</button>
                {showValue && (
                    <>
                        <p>Value: {review.value}</p>
                        <button type="submit">Submit</button>
                    </>
                )}
            </form>
        </div>
    );
};

export default AddReview;
