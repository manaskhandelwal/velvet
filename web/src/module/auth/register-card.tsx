"use client";

import { useForm, SubmitHandler } from "react-hook-form";
import { useRouter } from "next/navigation";
import { Label } from "../../components/ui/label";
import { Button } from "../../components/ui/button";
import {
  Card,
  CardHeader,
  CardTitle,
  CardContent,
  CardDescription,
} from "../../components/ui/card";
import { Input } from "../../components/ui/input";
import { API } from "../../utils/api";
import { useState } from "react";

interface RegisterCardProps {}

interface IRegisterFormInput {
  email: string;
  fullName: string;
  username: string;
  password: string;
}

interface IOtpFormInput {
  otp: number;
}

export const RegisterCard: React.FC<RegisterCardProps> = ({}) => {
  const [userRegistered, setUserRegistered] = useState(false);
  const router = useRouter();

  const RegisterForm = () => {
    const {
      register,
      handleSubmit,
      formState: { errors },
      setError,
    } = useForm<IRegisterFormInput>();

    const onSubmit: SubmitHandler<IRegisterFormInput> = async (data) => {
      try {
        const response = await API.post("/auth/register", {
          email: data.email,
          username: data.username,
          full_name: data.fullName,
          password: data.password,
        });

        const { access_token } = response.data;
        localStorage.setItem("access_token", access_token);
        setUserRegistered(true);
      } catch (error: any) {
        const err = error.response.data.detail;
        if (!err) return;

        if (err.target === "email") {
          setError("email", { message: err.msg });
        }

        if (err.target === "username") {
          setError("username", { message: err.msg });
        }
      }
    };

    return (
      <Card>
        <CardHeader>
          <CardTitle className={`text-2xl mb-4 text-center`}>
            Create your account
          </CardTitle>
        </CardHeader>
        <CardContent>
          <form className="space-y-2" onSubmit={handleSubmit(onSubmit)}>
            <div className={`flex flex-col gap-5 mb-10`}>
              <div className="space-y-1">
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  placeholder="john.doe@gmail.com"
                  {...register("email", {
                    required: "Email Address is required",
                  })}
                />
                {errors.email ? (
                  <p role="alert" className={`text-xs text-red-500`}>
                    {errors.email.message}
                  </p>
                ) : null}
              </div>

              <div className="space-y-1">
                <Label htmlFor="name">Full Name</Label>
                <Input
                  id="name"
                  placeholder="John Doe"
                  {...register("fullName", {
                    required: "Full Name is required",
                  })}
                />
                {errors.fullName ? (
                  <p role="alert" className={`text-xs text-red-500`}>
                    {errors.fullName.message}
                  </p>
                ) : null}
              </div>

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
              <Button>Register</Button>
            </div>
          </form>
        </CardContent>
      </Card>
    );
  };

  const OtpForm = () => {
    const [userVerified, setUserVerified] = useState(false);

    const {
      register,
      handleSubmit,
      formState: { errors },
      setError,
    } = useForm<IOtpFormInput>();

    const onSubmit: SubmitHandler<IOtpFormInput> = async (data) => {
      try {
        const responce = await API.post("/auth/verify-otp", {
          email_otp: Number(data.otp),
        });

        if (responce.data.success) {
          setUserVerified(true);

          setTimeout(() => {
            router.push("/profile/update");
          }, 1000);
        }
      } catch (error: any) {
        const err = error.response.data.detail;
        if (!err) return;

        if (err.target === "email-otp") {
          setError("otp", { message: err.msg });
        }
      }
    };

    return (
      <Card>
        <CardHeader>
          <CardTitle className={`text-2xl mb-4 text-center`}>
            Email Verification
          </CardTitle>
          <CardDescription>
            {!userVerified
              ? "Check your email for OTP. If you are not able to see it under 1 minute, then also check spam/junk mail."
              : "Redirecting you in 1 second!"}
          </CardDescription>
        </CardHeader>
        <CardContent>
          {!userVerified ? (
            <form className="space-y-2" onSubmit={handleSubmit(onSubmit)}>
              <div className={`flex flex-col gap-5 mb-10`}>
                <div className="space-y-1">
                  <Label htmlFor="otp">OTP (One Time Password)</Label>
                  <Input
                    id="otp"
                    placeholder="000000"
                    {...register("otp", {
                      required: "OTP (One Time Password) is required",
                    })}
                  />
                  {errors.otp ? (
                    <p role="alert" className={`text-xs text-red-500`}>
                      {errors.otp.message}
                    </p>
                  ) : null}
                </div>
              </div>

              <div className={`flex justify-center`}>
                <Button>Submit OTP</Button>
              </div>
            </form>
          ) : (
            <div
              className={`flex flex-col gap-10 justify-center items-center text-center mt-8`}
            >
              <span className={`text-7xl`}>✅</span>
              <p className={`text-2xl text-green-500 font-bold`}>
                Email verification successful
              </p>
            </div>
          )}
        </CardContent>
      </Card>
    );
  };

  return !userRegistered ? <RegisterForm /> : <OtpForm />;
};
