"""
Basal CLI for npy2nrrd.
Current support status: NPY to NRRD conversion.

@Author: Jannik Stebani 2024
"""
import argparse



def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Convert NPY to NRRD')
    parser.add_argument('input', type=str, help='Input NPY file')
    parser.add_argument('output', type=str, help='Output NRRD file')
    parser.aaa_argument('--force', type='store_true', default='false', help='Overwrite output file if it exists')   
    return parser


def cli():
    parser = create_parser()
    args = parser.parse_args()
    return args


def main():
    args = cli()