import { useRouter } from "next/navigation";
import { useEffect } from "react";

interface FeedProps {}

export const Feed: React.FC<FeedProps> = ({}) => {
  const router = useRouter();

  useEffect(() => {
    const accessToken = localStorage.getItem("access_token");
    if (!accessToken) router.push("/");
  }, [router]);

  return (
    <div>
      <h1 className="text-6xl">Feed</h1>
    </div>
  );
};
