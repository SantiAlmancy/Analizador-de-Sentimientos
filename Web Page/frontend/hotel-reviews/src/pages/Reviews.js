import React, {useEffect} from 'react';
import { useParams } from 'react-router-dom';

const Reviews = () => {
    const { id } = useParams();

    useEffect(() => {
        console.log(id)
    }, [id]); 

    return (
        <div>
            <h2>Reviews for Hotel ID: {id}</h2>
        </div>
    );
};

export default Reviews;
