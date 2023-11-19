"use client";

import { useForm, SubmitHandler } from "react-hook-form";

import { Label } from "../../components/ui/label";
import { Button } from "../../components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
} from "../../components/ui/card";
import { Input } from "../../components/ui/input";
import { API } from "../../utils/api";

interface LoginCardProps {}

interface ILoginFormInput {
  username: string;
  password: string;
}

export const LoginCard: React.FC<LoginCardProps> = ({}) => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<ILoginFormInput>();

  const onSubmit: SubmitHandler<ILoginFormInput> = async (data) => {
    try {
      const response = await API.post("/auth/login", {
        username: data.username,
        password: data.password,
      });

      const { access_token } = response.data;

      localStorage.setItem("access_token", access_token);
    } catch (error: any) {}
  };

  return (
    <Card>
      <CardHeader>
        <CardTitle className={`text-2xl mb-3 text-center`}>
          Login into your account
        </CardTitle>
      </CardHeader>
      <CardContent>
        <form className="space-y-2" onSubmit={handleSubmit(onSubmit)}>
          <div className={`flex flex-col gap-5 mb-10`}>
            <div className="space-y-1">
              <Label htmlFor="username">Username</Label>
              <Input
                id="username"
                placeholder="johndoe"
                {...register("username", {
                  required: "Username is required",
                })}
              />
              {errors.username ? (
                <p role="alert" className={`text-xs text-red-500`}>
                  {errors.username.message}
                </p>
              ) : null}
            </div>

            <div className="space-y-1">
              <Label htmlFor="password">Password</Label>
              <Input
                id="password"
                placeholder="really-secure-password"
                {...register("password", {
                  required: "Password is required",
                })}
              />
              {errors.password ? (
                <p role="alert" className={`text-xs text-red-500`}>
                  {errors.password.message}
                </p>
              ) : null}
            </div>
          </div>

          <div className={`flex justify-center`}>
            <Button>Login</Button>
          </div>
        </form>
      </CardContent>
    </Card>
  );
};
