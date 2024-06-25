import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Table from '../components/Table';
import Header from '../components/Header';
import ReviewText from '../components/ReviewText';
import AddReview from '../pages/AddReview';
import './Reviews.css';
import getReviews from '../services/ReviewService';

const Reviews = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [data, setData] = useState([])
    const [showForm, setShowForm] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
          try {
            const result = await getReviews(id);
            const modifiedData = result.map((item, index) => ({
              ...item,
              number: index + 1
            }));
            setData(modifiedData);
          } catch (err) {
            console.error(err);
          }
        };
    
        fetchData();
      }, [id]);

    const columns = [
        {
            name: "Nº",
            selector: (row) => row.number,
            sortable: true,
            maxWidth: "12%"
        },
        {
            name: "Value",
            selector: (row) => row.value,
            sortable: true,
            maxWidth: "14%"
        },
        {
            name: "Review",
            cell: (row) => <ReviewText text={row.review} />,
            sortable: true,
            maxWidth: "72%"
        }
    ];

    const handleButtonClick = () => {
        navigate(`/add-review/${id}`); 
        setShowForm(true);
    };

    const handleFormSubmit = (id, review) => {
        console.log(`Review submitted for Hotel ID ${id}:`, review);
        setShowForm(false);
    };

    return (
        <div className='reviews'>
            <Header text="Hotel Reviews" showButton={true}/>
            <div className='reviewList'>
                <h1>Review list for Hotel: {id}</h1>
                <button 
                    className="addReviewButton"
                    onClick={handleButtonClick}>
                    Add Review</button>
                <Table columns={columns} data={data} height={'520px'} />
                {showForm && <AddReview onSubmit={handleFormSubmit} />}
            </div>
        </div>
    );
};

export default Reviews;
