interface EvaluateButtonProps {
  onClick?: () => void;
  text?: string;
  isActive?: boolean;
}

export function EvaluateButton({
  onClick,
  text = 'Code Quality',
  isActive = false,
}: EvaluateButtonProps) {
  return (
    <button
      onClick={onClick}
      className={`
        inline-flex p-[11.226px_16.839px] flex-col items-start gap-[14.032px]
        rounded-[140.323px] border-[0.702px] border-[#6473A0]
        transition-all duration-200
        ${
          isActive
            ? 'bg-[#6473A0] text-white'
            : 'bg-[rgba(67,67,67,0.04)] text-[#6473A0] hover:bg-[rgba(67,67,67,0.08)]'
        }
        group
      `}
    >
      <div className='flex items-center gap-2'>
        {/* Plus sign in circle */}
        <div
          className={`
          w-6 h-6 rounded-full border-[0.702px] 
          ${isActive ? 'border-white' : 'border-[#6473A0]'}
          flex items-center justify-center
          transition-transform duration-300
          group-hover:rotate-90
        `}
        >
          <svg
            width='12'
            height='12'
            viewBox='0 0 12 12'
            fill='none'
            xmlns='http://www.w3.org/2000/svg'
            className='transition-transform duration-300'
          >
            <path
              d='M6 2.5V9.5M2.5 6H9.5'
              stroke={isActive ? 'white' : '#6473A0'}
              strokeWidth='1.5'
              strokeLinecap='round'
              strokeLinejoin='round'
            />
          </svg>
        </div>
        {/* Text */}
        <span
          className={`
          font-pretendard text-[15.435px] font-bold leading-[22.452px] tracking-[-0.386px]
          ${isActive ? 'text-white' : 'text-[#6473A0]'}
        `}
        >
          {text}
        </span>
      </div>
    </button>
  );
}
