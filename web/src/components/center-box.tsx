interface CenterBoxProps {
  children: React.ReactNode;
}

export const CenterBox: React.FC<CenterBoxProps> = ({ children }) => {
  return (
    <div className={`w-full h-full grid justify-center`}>
      <div className={`w-[400px]`}>{children}</div>
    </div>
  );
};
