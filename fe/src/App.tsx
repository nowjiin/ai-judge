import { BrowserRouter as Router } from 'react-router-dom';
import { Header } from './components/Header';
import { AppRoutes } from './routes';

function App() {
  return (
    <Router>
      <div className='min-h-screen relative'>
        {/* Gradient background */}
        <div
          className='fixed inset-0 animate-pulse-slow'
          style={{
            background: `
              linear-gradient(180deg, 
                rgba(116, 185, 255, 0.00) 0%,
                rgba(100, 115, 160, 0.39) 30%,
                rgba(100, 115, 160, 0.39) 70%,
                rgba(116, 185, 255, 0.00) 100%
              )
            `,
            zIndex: -1,
            animation: 'float 6s ease-in-out infinite',
          }}
        />
        <Header />
        <main className='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8'>
          <AppRoutes />
        </main>
      </div>
    </Router>
  );
}

export default App;
