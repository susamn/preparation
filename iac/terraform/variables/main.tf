provider "aws" {
  region = "us-east-1"
}

variable "vpc_name" {
  type        = string
  description = "This sets the vpc name"
}

variable "sshport" {
  type    = number
  default = 22
}

variable "enabled" {
  type    = bool
  default = true
}

variable "mylist" {
  type    = list(string)
  default = ["value1", "value2", "value3"]
}

variable "mymap" {
  type = map(string)
  default = {
    key1 = "value1"
    key2 = "value2"
    key3 = "value3"
  }
}

resource "aws_vpc" "myvpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = var.vpc_name
    Key1 = var.mylist[0]
    Key2 = var.mymap["key1"]
  }
}

output "vpcid" {
  value = aws_vpc.myvpc.id
}
