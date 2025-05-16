import { Button } from '../components/Button';
import { EvaluateButton } from '../components/EvaluateButton';
import { useState } from 'react';

export function HomePage() {
  const [isEvaluating, setIsEvaluating] = useState(false);

  return (
    <div className='flex flex-col items-center justify-center min-h-screen w-full'>
      <div className='flex flex-col items-center space-y-8 py-20'>
        <h2
          className='text-[60px] font-extrabold leading-normal text-[#6473A0] font-pretendard text-center animate-fade-in'
          style={{ animationDelay: '0.3s' }}
        >
          The fastest and most accurate way to evaluate your code
        </h2>
        <h1
          className='text-[120px] font-extrabold leading-normal text-black font-pretendard animate-fade-in'
          style={{ animationDelay: '0.6s' }}
        >
          Snapcode
        </h1>
        <div
          className='mt-12 flex items-center gap-4 animate-fade-in'
          style={{ animationDelay: '0.9s' }}
        >
          <Button>Snap my code</Button>
          <EvaluateButton checked={isEvaluating} onChange={setIsEvaluating} />
        </div>
      </div>
    </div>
  );
}
