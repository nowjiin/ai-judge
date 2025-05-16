interface EvaluateButtonProps {
  checked?: boolean;
  onChange?: (checked: boolean) => void;
}

export function EvaluateButton({
  checked = false,
  onChange,
}: EvaluateButtonProps) {
  return (
    <button
      onClick={() => onChange?.(!checked)}
      className={`
        inline-flex p-[11.226px_16.839px] flex-col items-start gap-[14.032px]
        rounded-[140.323px] border-[0.702px] border-[#6473A0]
        bg-[rgba(67,67,67,0.04)] transition-all duration-200
        hover:bg-[rgba(67,67,67,0.08)]
      `}
    >
      <div className='flex items-center gap-2'>
        {/* Plus sign */}
        <div className='w-4 h-4 flex items-center justify-center'>
          <svg
            width='16'
            height='16'
            viewBox='0 0 16 16'
            fill='none'
            xmlns='http://www.w3.org/2000/svg'
          >
            <path
              d='M8 3.33334V12.6667M3.33333 8H12.6667'
              stroke='#6473A0'
              strokeWidth='1.5'
              strokeLinecap='round'
              strokeLinejoin='round'
            />
          </svg>
        </div>
        {/* Checkbox */}
        <div
          className={`
          w-4 h-4 rounded border-[0.702px] border-[#6473A0]
          flex items-center justify-center
          ${checked ? 'bg-[#6473A0]' : 'bg-transparent'}
        `}
        >
          {checked && (
            <svg
              width='12'
              height='12'
              viewBox='0 0 12 12'
              fill='none'
              xmlns='http://www.w3.org/2000/svg'
            >
              <path
                d='M2 6L4.5 8.5L10 3'
                stroke='white'
                strokeWidth='1.5'
                strokeLinecap='round'
                strokeLinejoin='round'
              />
            </svg>
          )}
        </div>
      </div>
    </button>
  );
}
