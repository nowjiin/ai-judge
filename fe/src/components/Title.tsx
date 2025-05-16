interface TitleProps {
  children: React.ReactNode;
}

export function Title({ children }: TitleProps) {
  return (
    <h1 className='text-[50px] font-extrabold leading-normal text-black font-pretendard'>
      {children}
    </h1>
  );
}
