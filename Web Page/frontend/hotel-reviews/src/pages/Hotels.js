import React from 'react';
import Header from '../components/Header';
import Banner from '../components/Banner';
import './Hotels.css';

const Hotels = () => {
    return (
        <div className='hotels'>
            <Header text="Hotel Reviews" />
            <Banner/>
            <div className='hotelList'>
                <h1>List of hotels</h1>
            </div>
        </div>
    );
}

export default Hotels;
