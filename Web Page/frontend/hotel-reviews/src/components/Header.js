import React from 'react';
import { useNavigate  } from 'react-router-dom';
import './Header.css';

const Header = (props) => {
    const navigate = useNavigate();

    const handleBackClick = () => {
        navigate(-1);
    };

    return (
        <div className="rectangle">
            <span className="yellow-text">{props.text}</span>
            {props.showButton && <button className="button" onClick={handleBackClick}>Go Back</button>}
        </div>
    );
}

export default Header;