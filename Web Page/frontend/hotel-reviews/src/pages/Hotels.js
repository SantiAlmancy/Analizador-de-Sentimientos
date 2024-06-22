import React, { useState } from 'react';
import Header from '../components/Header';
import Banner from '../components/Banner';
import './Hotels.css';
import Table from '../components/Table';

const Hotels = () => {
    const [clickedButtonId, setClickedButtonId] = useState(null);

    const data = [
        { "id": 1, "name": "Hotel California", "hotel_class": 3 },
        { "id": 2, "name": "Grand Budapest Hotel", "hotel_class": 5 },
        { "id": 3, "name": "Hotel 3", "hotel_class": 4 },
        { "id": 4, "name": "Hotel 4", "hotel_class": 1 },
        { "id": 5, "name": "Hotel 5", "hotel_class": 4 },
        { "id": 6, "name": "Hotel 6", "hotel_class": 4 },
        { "id": 7, "name": "Hotel 7", "hotel_class": 4 },
        { "id": 8, "name": "Hotel 8", "hotel_class": 4 },
        { "id": 9, "name": "Hotel 9", "hotel_class": 4 },
        { "id": 10, "name": "Hotel 10", "hotel_class": 4 },
        { "id": 11, "name": "Hotel 11", "hotel_class": 4 }
    ];

    const handleButtonClick = (id) => {
        console.log(`Clicked ID: ${id}`);
        setClickedButtonId(id);
    };

    const columns = [
        {
            name: "Id",
            selector: (row) => row.id,
            sortable: true
        },
        {
            name: "Name",
            selector: (row) => row.name,
            sortable: true
        },
        {
            name: "Class",
            selector: (row) => row.hotel_class,
            sortable: true
        },
        {
            name: "Action",
            cell: row => (
                <button 
                    className={`rowButton ${clickedButtonId === row.id ? 'clicked' : ''}`}
                    onClick={() => handleButtonClick(row.id)}
                >
                    Reviews
                </button>
            )
        }
    ];

    return (
        <div className='hotels'>
            <Header text="Hotel Reviews" />
            <Banner />
            <div className='hotelList'>
                <h1>Hotel list</h1>
                <Table columns={columns} data={data} />
            </div>
        </div>
    );
};

export default Hotels;
