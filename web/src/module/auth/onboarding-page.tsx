"use client";
import { useRouter } from "next/navigation";
import {
  Tabs,
  TabsList,
  TabsTrigger,
  TabsContent,
} from "../../components/ui/tabs";
import { CenterBox } from "../../components/center-box";
import { LoginCard } from "./login-card";
import { RegisterCard } from "./register-card";
import { Logo } from "../../components/logo";
import { useEffect, useState } from "react";

interface OnboardingPageProps {}

export const OnboardingPage: React.FC<OnboardingPageProps> = ({}) => {
  const router = useRouter();

  useEffect(() => {
    const accessToken = localStorage.getItem("access_token");
    if (accessToken) router.push("/feed");
  }, [router]);

  return (
    <section className={`min-h-screen min-w-screen py-20`}>
      <CenterBox>
        <div className={`mb-10 flex justify-center`}>
          <Logo />
        </div>
        <Tabs defaultValue="register">
          <TabsList className="grid w-full grid-cols-2">
            <TabsTrigger value="register">Register</TabsTrigger>
            <TabsTrigger value="login">Login</TabsTrigger>
          </TabsList>

          <TabsContent value="register">
            <RegisterCard />
          </TabsContent>

          <TabsContent value="login">
            <LoginCard />
          </TabsContent>
        </Tabs>
      </CenterBox>
    </section>
  );
};
