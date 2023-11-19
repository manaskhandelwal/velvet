import Image from "next/image";

interface LogoProps {}

export const Logo: React.FC<LogoProps> = ({}) => {
  return (
    <div>
      <Image
        alt="velvet logo"
        src={"/logo-light.png"}
        width={140}
        height={84}
      />
    </div>
  );
};
// 5:3
// 140
