import { Link } from 'react-router-dom';

export function Header() {
  return (
    <header className='bg-white border-b border-gray-200'>
      <nav className='max-w-7xl mx-auto px-8'>
        <div className='flex justify-between h-16'>
          {/* Logo and brand name */}
          <div className='flex items-center'>
            <div className='flex-shrink-0'>
              <Link
                to='/'
                className='text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent'
              >
                SnapCode
              </Link>
            </div>
          </div>

          {/* Navigation */}
          <div className='flex items-center space-x-8'>
            <Link
              to='/'
              className='text-gray-700 hover:text-indigo-600 px-3 py-2 text-sm font-bold transition-colors duration-200'
            >
              Home
            </Link>
            <Link
              to='/business'
              className='text-gray-700 hover:text-indigo-600 px-3 py-2 text-sm font-bold transition-colors duration-200'
            >
              Business
            </Link>
            <Link
              to='/personal'
              className='text-gray-700 hover:text-indigo-600 px-3 py-2 text-sm font-bold transition-colors duration-200'
            >
              Personal
            </Link>
            <Link
              to='/mypage'
              className='flex items-center text-gray-700 hover:text-indigo-600 px-3 py-2 text-sm font-bold transition-colors duration-200'
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
      </nav>
    </header>
  );
}
