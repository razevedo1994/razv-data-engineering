terraform {
  required_version = ">= 1.0.0, < 2.0.0"

  required_providers {
    aws = {
        sosource = "hashicorp/aws"
        version  = "~> 4.0" 
    }
  }
}

resource "aws_launch_configuration" "example" {
  image_id          = "ami-0fb653ca2d3203ac1"
  instance_type     = var.instance_type
  security_groups   = [aws_security_group.instance.id]

  user_data = templatefile("${path.module}/user-data.sh", {
    server_port = var.server_port
    db_address  = data.terraform_remote_state.db.outputs.address
    db_port     = data.terraform_remote_state.db.outputs.port
  })

  # Required when using a launch configuration with an auto scaling group.
  lifecycle {
    create_before_destroy = true
}

resource "aws_autoscaling_group" "example" {
  launch_configuration  = aws_launch_configuration.example.name
  vpc_zone_identifier   = data.aws_subnets.default.ids
  target_group_arns     = [aws_lb_target_group.asg.arn]
  health_check_type     = "ELB"

  min_size = var.min_size
  max_size = var.max_size

  tag {
    key                 = "Name"
    value               = var.cluster_name
    propagate_at_launch = true
  }
}

resource "aws_security_group" "instance" {
  name = "${var.cluster_name}-instance"
}

