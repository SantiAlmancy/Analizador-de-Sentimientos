import { Route, Routes } from 'react-router-dom';
import './App.css';
import Hotels from './pages/Hotels';
import Reviews from './pages/Reviews';
import AddReview from './pages/AddReview';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Hotels/>}/>
        <Route path="/reviews/:id" element={<Reviews />} />
        <Route path="/add-review/:id" element={<AddReview />} />
      </Routes>
    </div>
  );
}

export default App;
