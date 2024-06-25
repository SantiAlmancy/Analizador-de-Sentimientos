import React from 'react';
import './Banner.css';

const Banner = () => {
    return (
        <div className="banner-container">
            <div className="image-overlay">
            <div className="text-container">
                    <span className="title-banner-text">Rate My Stay</span>
                    <span className="banner-text">Explore our platform to discover a curated selection of hotels and insightful guest reviews. Find your perfect stay with comprehensive information and authentic feedback from fellow travelers. Delve into detailed descriptions and unbiased recommendations to make informed decisions about your next destination.</span>
                </div>
            </div>
            <img src={'/assets/images/banner1.jpg'} alt="Banner" className="banner-image" />
        </div>
    );
}

export default Banner;
