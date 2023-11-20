import { useRouter } from "next/navigation";
import { useEffect } from "react";
import { Header } from "./header";

interface FeedProps {}

export const Feed: React.FC<FeedProps> = ({}) => {
  const router = useRouter();

  useEffect(() => {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) router.push("/");
  }, [router]);

  return (
    <div>
      <Header />
      <h1 className="text-6xl">Feed</h1>
    </div>
  );
};
