import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import Table from '../components/Table';
import Header from '../components/Header';
import ReviewText from '../components/ReviewText';
import AddReview from '../pages/AddReview';
import './Reviews.css';

const Reviews = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [showForm, setShowForm] = useState(false);

    useEffect(() => {
        console.log(id);
    }, [id]);

    const data = [
        {
            idReview: 1,
            value: "Negative",
            text: 'The hotel has a great location The rooms are noisy. The rooms have no carpeting on the floors. If someone in the room above drops a penny or moves a chair it is clearly heard in the room below.'
        },
        {
            idReview: 2,
            value: "Positive",
            text: 'Definitely one of the better Best Westerns around. We liked the location near the University of Washington, and the view from our room on the seventh floor was great. The rooms look like they were decorated on the "trading spaces" tv show--not the most luxurious or highest quality of furnishings, but very thoughtful and creative. There are cheaper, adequate lodging options available in Seattle, but this hotel is still a good value.'
        },
        {
            idReview: 3,
            value: "Positive",
            text: 'Wow!!!!! A great hotel at a really reasonable price and very convenient to the University of Washington. I stayed here for two nights during a conference at the end of January 2005 and spent $79 per night for one of their studio rooms. Everywhere was neat and clean and looked like it had been recently renovated. While the studio room was on the small side, it was plenty big enough for what I needed. Double bed, desk, two drawer dresser, tv, huge walk in closet, iron, ironing board and nice large windows. The only complaint was that the bathroom was small and that made it tough to close the door (no clearance between the door and toilet). Continental breakfast was very nice with yogurt, cold cereals, instant oatmeal, bagels, english muffins, danishes, muffins, fruit, hard boiled eggs and beverages. Free internet access in the lobby and business center with free Wi-Fi in the lobby and lots of comfy couches and chairs in the lobby Fitness center and bar/restaurant in the basement. Front desk staff were all very friendly and helpful and were able to give lots of advice on local restaurants. Definitely a great value and right next to the University of Washington.'
        },
        {
            idReview: 4,
            value: "Negative",
            text: "Old hotel, superficial remodeling of public areas that are dark and uncomfortable, small room, less than 200 sqft, tiny bathroom with original 1930's fixtures, no counter space, toilet tank cover cracked and patched, cracked paint on original doors, dim bedside lamps, wobbly elevators. Alltogether a bad experience, certainly not worth the price."
        },
        {
            idReview: 5,
            value: "Positive",
            text: 'Great service, clean rooms, friendly staff. They helped us get around the city, made recommendations for restaurants, and overall were a great help.'
        }
    ];

    const columns = [
        {
            name: "Id",
            selector: (row) => row.idReview,
            sortable: true,
            maxWidth: "13%"
        },
        {
            name: "Value",
            selector: (row) => row.value,
            sortable: true,
            maxWidth: "14%"
        },
        {
            name: "Review",
            cell: (row) => <ReviewText text={row.text} />,
            sortable: true,
            maxWidth: "70%"
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
            <Header text="Reviews" />
            <div className='reviewList'>
                <h1>Review list for Hotel: {id}</h1>
                <Table columns={columns} data={data} height={'520px'} />
                <button 
                    className="rowButton"
                    onClick={handleButtonClick}>
                    Add Review</button>
                {showForm && <AddReview onSubmit={handleFormSubmit} />}
            </div>
        </div>
    );
};

export default Reviews;
