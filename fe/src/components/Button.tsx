interface ButtonProps {
  disabled?: boolean;
  onClick?: () => void;
  children: React.ReactNode;
}

export function Button({ disabled = false, onClick, children }: ButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={`
        flex w-[229px] h-[76px] p-[10px] justify-center items-center gap-[10px]
        rounded-[14px] font-pretendard text-[24px] font-semibold leading-[22.452px]
        tracking-[-0.6px] transition-all duration-200
        ${
          disabled
            ? 'border-[0.5px] border-white bg-[rgba(116,185,255,0.24)] text-[rgba(154,154,154,0.45)] font-bold'
            : 'bg-[#6473A0] text-white hover:bg-[#55628A] active:bg-[#4A5678]'
        }
      `}
    >
      {children}
    </button>
  );
}
