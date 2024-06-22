import { Route, Routes } from 'react-router-dom';
import './App.css';
import Hotels from './pages/Hotels';
import Reviews from './pages/Reviews';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<Hotels/>}/>
        <Route path="/reviews/:id" element={<Reviews />} />
      </Routes>
    </div>
  );
}

export default App;
