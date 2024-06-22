import React from 'react';
import './Header.css';

const Header = (props) => {
    return (
        <div className="rectangle">
            <span className="yellow-text">{props.text}</span>
        </div>
    );
}

export default Header;
