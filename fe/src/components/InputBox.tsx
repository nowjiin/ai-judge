interface InputBoxProps {
  title: string;
  name: string;
  type?: 'text' | 'password' | 'email' | 'number';
  required?: boolean;
  placeholder?: string;
  value?: string;
  onChange?: (value: string) => void;
}

export function InputBox({
  title,
  name,
  type = 'text',
  required = false,
  placeholder = '',
  value = '',
  onChange,
}: InputBoxProps) {
  return (
    <div className='space-y-2'>
      <label
        htmlFor={name}
        className='block text-[38.31px] font-bold leading-normal text-[#00002E] font-pretendard'
      >
        {title}
        {required && <span className='text-red-500 ml-1'>*</span>}
      </label>
      <input
        type={type}
        name={name}
        id={name}
        value={value}
        onChange={(e) => onChange?.(e.target.value)}
        placeholder={placeholder}
        required={required}
        className='block w-full rounded-[7.662px] bg-[#ECECEC] px-3 py-2 text-[16px] leading-[30.648px] text-[#A1A1A1] font-pretendard font-normal placeholder:text-[#A1A1A1] focus:outline-none'
      />
    </div>
  );
}
