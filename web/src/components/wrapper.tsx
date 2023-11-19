import clsx from "clsx";

interface WrapperProps {
  children: React.ReactNode;
  className?: string;
}

export const Wrapper: React.FC<WrapperProps> = ({ children, className }) => {
  return (
    <section className={clsx(`w-[65vw] mx-auto`, className)}>
      {children}
    </section>
  );
};
