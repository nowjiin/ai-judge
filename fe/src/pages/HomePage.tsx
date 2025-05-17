import { Button } from '../components/Button';

export function HomePage() {
  return (
    <div className='relative w-full min-h-[calc(100vh-4rem)] overflow-x-hidden'>
      {/* Gradient background */}
      <div
        className='fixed inset-0 w-screen'
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
        }}
      />
      <div className='flex flex-col items-center justify-center w-full h-full py-12 px-4'>
        <div className='flex flex-col items-center space-y-8'>
          <h2
            className='text-4xl md:text-[60px] font-extrabold leading-tight md:leading-normal text-[#6473A0] font-pretendard text-center animate-fade-in'
            style={{ animationDelay: '0.3s' }}
          >
            내 코드를 평가받는 가장 빠르고 정확한 방법
          </h2>
          <h1
            className='text-6xl md:text-[120px] font-extrabold leading-tight md:leading-normal text-black font-pretendard animate-fade-in'
            style={{ animationDelay: '0.6s' }}
          >
            Snapcode
          </h1>
          <div
            className='mt-8 md:mt-12 flex flex-col items-center gap-4 animate-fade-in'
            style={{ animationDelay: '0.9s' }}
          >
            <Button>Snap my code</Button>
          </div>
        </div>
      </div>
    </div>
  );
}
