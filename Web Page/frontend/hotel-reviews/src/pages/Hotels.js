import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Header from '../components/Header';
import Banner from '../components/Banner';
import Table from '../components/Table';
import getHotels from '../services/HotelService';
import './Hotels.css';

const Hotels = () => {
    const navigate = useNavigate();

    const [data, setData] = useState([])

    useEffect(() => {
        const fetchData = async () => {
          try {
            const result = await getHotels();
            setData(result);
            console.log(result);
          } catch (err) {
            console.error(err);
          }
        };
    
        fetchData();
      }, []);

    const handleButtonClick = (id) => {
        navigate(`/reviews/${id}`); 
    };

    const columns = [
        {
            name: "Id",
            selector: (row) => row.hotel_id,
            sortable: true,
            width: "13%"
        },
        {
            name: "Class",
            selector: (row) => row.hotel_class,
            sortable: true,
            width: "13%"
        },
        {
            name: "Name",
            selector: (row) => row.hotel_name,
            sortable: true,
            width: "57%"
        },
        {
            name: "Action",
            cell: row => (
                <button 
                    className="rowButton"
                    onClick={() => handleButtonClick(row.hotel_id)}
                >
                    Reviews
                </button>
            )
        }
    ];

    return (
        <div className='hotels'>
            <Header text="Hotel Reviews" showButton={false}/>
            <Banner />
            <div className='hotelList'>
                <h1>Hotel list</h1>
                <Table columns={columns} data={data} height={'475px'} />
            </div>
        </div>
    );
};

export default Hotels;
