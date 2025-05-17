import { Link } from 'react-router-dom';
import { useState } from 'react';

export function Header() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <header className='bg-white border-b border-gray-200'>
      <nav className='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8'>
        <div className='flex justify-between h-16'>
          {/* Logo and brand name */}
          <div className='flex items-center'>
            <div className='flex-shrink-0'>
              <Link
                to='/'
                className='text-2xl font-pretendard font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent'
              >
                SnapCode
              </Link>
            </div>
          </div>

          {/* Mobile menu button */}
          <div className='flex items-center sm:hidden'>
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className='inline-flex items-center justify-center p-2 rounded-md text-gray-700 hover:text-indigo-600 focus:outline-none'
            >
              <svg
                className='h-6 w-6'
                fill='none'
                viewBox='0 0 24 24'
                stroke='currentColor'
              >
                {isMenuOpen ? (
                  <path
                    strokeLinecap='round'
                    strokeLinejoin='round'
                    strokeWidth={2}
                    d='M6 18L18 6M6 6l12 12'
                  />
                ) : (
                  <path
                    strokeLinecap='round'
                    strokeLinejoin='round'
                    strokeWidth={2}
                    d='M4 6h16M4 12h16M4 18h16'
                  />
                )}
              </svg>
            </button>
          </div>

          {/* Desktop Navigation */}
          <div className='hidden sm:flex sm:items-center sm:space-x-4'>
            <Link
              to='/business'
              className='font-pretendard text-gray-700 hover:text-indigo-600 px-2 py-2 text-sm font-bold transition-colors duration-200'
            >
              Business
            </Link>
            <Link
              to='/personal'
              className='font-pretendard text-gray-700 hover:text-indigo-600 px-2 py-2 text-sm font-bold transition-colors duration-200'
            >
              Personal
            </Link>
            <Link
              to='/mypage'
              className='flex items-center font-pretendard text-gray-700 hover:text-indigo-600 px-2 py-2 text-sm font-bold transition-colors duration-200'
            >
              <svg
                className='w-5 h-5 mr-1'
                fill='none'
                stroke='currentColor'
                viewBox='0 0 24 24'
                xmlns='http://www.w3.org/2000/svg'
              >
                <path
                  strokeLinecap='round'
                  strokeLinejoin='round'
                  strokeWidth={2}
                  d='M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z'
                />
              </svg>
              MyPage
            </Link>
          </div>
        </div>

        {/* Mobile Navigation */}
        {isMenuOpen && (
          <div className='sm:hidden'>
            <div className='pt-2 pb-3 space-y-1'>
              <Link
                to='/business'
                className='block font-pretendard text-gray-700 hover:text-indigo-600 px-3 py-2 text-base font-bold transition-colors duration-200'
              >
                Business
              </Link>
              <Link
                to='/personal'
                className='block font-pretendard text-gray-700 hover:text-indigo-600 px-3 py-2 text-base font-bold transition-colors duration-200'
              >
                Personal
              </Link>
              <Link
                to='/mypage'
                className='flex items-center font-pretendard text-gray-700 hover:text-indigo-600 px-3 py-2 text-base font-bold transition-colors duration-200'
              >
                <svg
                  className='w-5 h-5 mr-2'
                  fill='none'
                  stroke='currentColor'
                  viewBox='0 0 24 24'
                  xmlns='http://www.w3.org/2000/svg'
                >
                  <path
                    strokeLinecap='round'
                    strokeLinejoin='round'
                    strokeWidth={2}
                    d='M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z'
                  />
                </svg>
                MyPage
              </Link>
            </div>
          </div>
        )}
      </nav>
    </header>
  );
}
