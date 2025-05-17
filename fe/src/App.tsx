import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Header } from './components/Header';
import { HomePage } from './pages/HomePage';
import { PersonalPage } from './pages/PersonalPage';

export function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/personal' element={<PersonalPage />} />
      </Routes>
    </Router>
  );
}
