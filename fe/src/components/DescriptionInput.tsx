import type { ChangeEvent } from 'react';

interface DescriptionInputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  maxLength?: number;
  title?: string;
  required?: boolean;
}

export function DescriptionInput({
  value,
  onChange,
  placeholder = 'Enter description...',
  maxLength = 1000,
  title,
  required = false,
}: DescriptionInputProps) {
  const handleChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    onChange(e.target.value);
  };

  return (
    <div className='w-full'>
      {title && (
        <div className='mb-2'>
          <div className='font-pretendard text-[20px] font-medium leading-[28px] tracking-[-0.386px] text-[#6473A0] flex items-start'>
            <span className='align-top'>{title}</span>
            {required && (
              <span className='text-red-500 text-[8px] ml-1 leading-none align-top'>
                *
              </span>
            )}
          </div>
        </div>
      )}
      <textarea
        value={value}
        onChange={handleChange}
        placeholder={placeholder}
        maxLength={maxLength}
        required={required}
        className={`
          w-full min-h-[120px] p-4
          rounded-lg border-[0.702px]
          bg-[rgba(67,67,67,0.04)]
          text-[#6473A0] placeholder-[#6473A0]/50
          font-pretendard text-[15.435px] leading-[22.452px] tracking-[-0.386px]
          resize-none
          transition-all duration-200
          focus:outline-none focus:border-[#6473A0] focus:bg-[rgba(67,67,67,0.08)]
          hover:bg-[rgba(67,67,67,0.08)]
        `}
      />
      <div className='mt-2 text-right'>
        <span className='text-[#6473A0] text-sm'>
          {value.length}/{maxLength}
        </span>
      </div>
    </div>
  );
}
