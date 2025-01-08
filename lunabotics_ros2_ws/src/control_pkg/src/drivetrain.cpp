#include "rclcpp/rclcpp.hpp"
#include "interfaces_pkg/msg/duty_cycle_output.hpp"

class DrivetrainNode : public rclcpp::Node
{
	public:
		DrivetrainNode()
		: Node("drivetrain") {
			test_control_subscriber = this->create_subscription<interfaces_pkg::msg::DutyCycleOutput>(
      "drivetrain/duty_cycle", 10, std::bind(&DrivetrainNode::duty_cycle_control, this, std::placeholders::_1));
		}
		
	private:
		void duty_cycle_control(const interfaces_pkg::msg::DutyCycleOutput & msg) const {
			RCLCPP_INFO(this->get_logger(), "%f %f %f %f %f %f", msg.left_drive_output, msg.right_drive_output, msg.left_lift_output, msg.right_lift_output, msg.tilt_output, msg.vibrator_output);
		}
		
		rclcpp::Subscription<interfaces_pkg::msg::DutyCycleOutput>::SharedPtr test_control_subscriber;
		
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<DrivetrainNode>());
  rclcpp::shutdown();
  return 0;
}


