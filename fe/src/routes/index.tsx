import { Routes, Route } from 'react-router-dom';
import { PersonalPage } from '../pages/PersonalPage';
import { HomePage } from '../pages/HomePage';

export function AppRoutes() {
  return (
    <Routes>
      <Route path='/' element={<HomePage />} />
      <Route path='/business' element={<div>Business Page</div>} />
      <Route path='/personal' element={<PersonalPage />} />
      <Route path='/mypage' element={<div>My Page</div>} />
    </Routes>
  );
}
