from tensorboardX import SummaryWriter

writer = None


def get_writer():
    """Create global writer object."""
    global writer
    if not writer:
        writer = SummaryWriter('./logs/cnn_mnist', flush_secs=5)


def write_metric(node_name, task_name, metric_name, metric, round_number):
    """Write metric callback."""
    get_writer()
    writer.add_scalar(f'{node_name}/{task_name}/{metric_name}', metric, round_number)
